/*
 * clearconsensus-sdk
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * TitaniumPage
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-08-23T14:39:24.626712Z[UTC]")
public class TitaniumPage {
  public static final String SERIALIZED_NAME_PAGE_NUMBER = "pageNumber";
  @SerializedName(SERIALIZED_NAME_PAGE_NUMBER)
  private Integer pageNumber;

  public static final String SERIALIZED_NAME_SIZE = "size";
  @SerializedName(SERIALIZED_NAME_SIZE)
  private Integer size;

  public static final String SERIALIZED_NAME_TOTAL_NUMBER_OF_ELEMENTS = "totalNumberOfElements";
  @SerializedName(SERIALIZED_NAME_TOTAL_NUMBER_OF_ELEMENTS)
  private String totalNumberOfElements;

  public TitaniumPage() { 
  }

  public TitaniumPage pageNumber(Integer pageNumber) {
    
    this.pageNumber = pageNumber;
    return this;
  }

   /**
   * Get pageNumber
   * @return pageNumber
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Integer getPageNumber() {
    return pageNumber;
  }


  public void setPageNumber(Integer pageNumber) {
    this.pageNumber = pageNumber;
  }


  public TitaniumPage size(Integer size) {
    
    this.size = size;
    return this;
  }

   /**
   * Get size
   * @return size
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Integer getSize() {
    return size;
  }


  public void setSize(Integer size) {
    this.size = size;
  }


  public TitaniumPage totalNumberOfElements(String totalNumberOfElements) {
    
    this.totalNumberOfElements = totalNumberOfElements;
    return this;
  }

   /**
   * Get totalNumberOfElements
   * @return totalNumberOfElements
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getTotalNumberOfElements() {
    return totalNumberOfElements;
  }


  public void setTotalNumberOfElements(String totalNumberOfElements) {
    this.totalNumberOfElements = totalNumberOfElements;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumPage titaniumPage = (TitaniumPage) o;
    return Objects.equals(this.pageNumber, titaniumPage.pageNumber) &&
        Objects.equals(this.size, titaniumPage.size) &&
        Objects.equals(this.totalNumberOfElements, titaniumPage.totalNumberOfElements);
  }

  @Override
  public int hashCode() {
    return Objects.hash(pageNumber, size, totalNumberOfElements);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumPage {\n");
    sb.append("    pageNumber: ").append(toIndentedString(pageNumber)).append("\n");
    sb.append("    size: ").append(toIndentedString(size)).append("\n");
    sb.append("    totalNumberOfElements: ").append(toIndentedString(totalNumberOfElements)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("pageNumber");
    openapiFields.add("size");
    openapiFields.add("totalNumberOfElements");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumPage
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumPage.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumPage is not found in the empty JSON string", TitaniumPage.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumPage.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumPage` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("totalNumberOfElements") != null && !jsonObj.get("totalNumberOfElements").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `totalNumberOfElements` to be a primitive type in the JSON string but got `%s`", jsonObj.get("totalNumberOfElements").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumPage.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumPage' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumPage> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumPage.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumPage>() {
           @Override
           public void write(JsonWriter out, TitaniumPage value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumPage read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumPage given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumPage
  * @throws IOException if the JSON string is invalid with respect to TitaniumPage
  */
  public static TitaniumPage fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumPage.class);
  }

 /**
  * Convert an instance of TitaniumPage to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

