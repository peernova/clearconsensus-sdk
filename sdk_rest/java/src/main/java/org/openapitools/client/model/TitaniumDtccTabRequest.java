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
import org.openapitools.client.model.TitaniumFilterPack;
import org.openapitools.client.model.TitaniumOrderBy;
import org.openapitools.client.model.TitaniumPage;
import org.openapitools.client.model.TitaniumSubGroupKeySearch;

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
 * TitaniumDtccTabRequest
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-08-18T13:00:58.962458Z[UTC]")
public class TitaniumDtccTabRequest {
  public static final String SERIALIZED_NAME_ASSET_ID = "assetId";
  @SerializedName(SERIALIZED_NAME_ASSET_ID)
  private String assetId;

  public static final String SERIALIZED_NAME_FILTER_PACK = "filterPack";
  @SerializedName(SERIALIZED_NAME_FILTER_PACK)
  private TitaniumFilterPack filterPack;

  public static final String SERIALIZED_NAME_ORDER_BY = "orderBy";
  @SerializedName(SERIALIZED_NAME_ORDER_BY)
  private TitaniumOrderBy orderBy;

  public static final String SERIALIZED_NAME_PAGE = "page";
  @SerializedName(SERIALIZED_NAME_PAGE)
  private TitaniumPage page;

  public static final String SERIALIZED_NAME_SNAP_DATE = "snapDate";
  @SerializedName(SERIALIZED_NAME_SNAP_DATE)
  private String snapDate;

  public static final String SERIALIZED_NAME_SUB_GROUP_KEY_SEARCH = "subGroupKeySearch";
  @SerializedName(SERIALIZED_NAME_SUB_GROUP_KEY_SEARCH)
  private TitaniumSubGroupKeySearch subGroupKeySearch;

  public static final String SERIALIZED_NAME_SUBMISSION_ID = "submissionId";
  @SerializedName(SERIALIZED_NAME_SUBMISSION_ID)
  private String submissionId;

  public static final String SERIALIZED_NAME_TRACE_NAME = "traceName";
  @SerializedName(SERIALIZED_NAME_TRACE_NAME)
  private String traceName;

  public TitaniumDtccTabRequest() { 
  }

  public TitaniumDtccTabRequest assetId(String assetId) {
    
    this.assetId = assetId;
    return this;
  }

   /**
   * Get assetId
   * @return assetId
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getAssetId() {
    return assetId;
  }


  public void setAssetId(String assetId) {
    this.assetId = assetId;
  }


  public TitaniumDtccTabRequest filterPack(TitaniumFilterPack filterPack) {
    
    this.filterPack = filterPack;
    return this;
  }

   /**
   * Get filterPack
   * @return filterPack
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumFilterPack getFilterPack() {
    return filterPack;
  }


  public void setFilterPack(TitaniumFilterPack filterPack) {
    this.filterPack = filterPack;
  }


  public TitaniumDtccTabRequest orderBy(TitaniumOrderBy orderBy) {
    
    this.orderBy = orderBy;
    return this;
  }

   /**
   * Get orderBy
   * @return orderBy
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumOrderBy getOrderBy() {
    return orderBy;
  }


  public void setOrderBy(TitaniumOrderBy orderBy) {
    this.orderBy = orderBy;
  }


  public TitaniumDtccTabRequest page(TitaniumPage page) {
    
    this.page = page;
    return this;
  }

   /**
   * Get page
   * @return page
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumPage getPage() {
    return page;
  }


  public void setPage(TitaniumPage page) {
    this.page = page;
  }


  public TitaniumDtccTabRequest snapDate(String snapDate) {
    
    this.snapDate = snapDate;
    return this;
  }

   /**
   * Get snapDate
   * @return snapDate
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getSnapDate() {
    return snapDate;
  }


  public void setSnapDate(String snapDate) {
    this.snapDate = snapDate;
  }


  public TitaniumDtccTabRequest subGroupKeySearch(TitaniumSubGroupKeySearch subGroupKeySearch) {
    
    this.subGroupKeySearch = subGroupKeySearch;
    return this;
  }

   /**
   * Get subGroupKeySearch
   * @return subGroupKeySearch
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public TitaniumSubGroupKeySearch getSubGroupKeySearch() {
    return subGroupKeySearch;
  }


  public void setSubGroupKeySearch(TitaniumSubGroupKeySearch subGroupKeySearch) {
    this.subGroupKeySearch = subGroupKeySearch;
  }


  public TitaniumDtccTabRequest submissionId(String submissionId) {
    
    this.submissionId = submissionId;
    return this;
  }

   /**
   * Get submissionId
   * @return submissionId
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getSubmissionId() {
    return submissionId;
  }


  public void setSubmissionId(String submissionId) {
    this.submissionId = submissionId;
  }


  public TitaniumDtccTabRequest traceName(String traceName) {
    
    this.traceName = traceName;
    return this;
  }

   /**
   * Get traceName
   * @return traceName
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getTraceName() {
    return traceName;
  }


  public void setTraceName(String traceName) {
    this.traceName = traceName;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumDtccTabRequest titaniumDtccTabRequest = (TitaniumDtccTabRequest) o;
    return Objects.equals(this.assetId, titaniumDtccTabRequest.assetId) &&
        Objects.equals(this.filterPack, titaniumDtccTabRequest.filterPack) &&
        Objects.equals(this.orderBy, titaniumDtccTabRequest.orderBy) &&
        Objects.equals(this.page, titaniumDtccTabRequest.page) &&
        Objects.equals(this.snapDate, titaniumDtccTabRequest.snapDate) &&
        Objects.equals(this.subGroupKeySearch, titaniumDtccTabRequest.subGroupKeySearch) &&
        Objects.equals(this.submissionId, titaniumDtccTabRequest.submissionId) &&
        Objects.equals(this.traceName, titaniumDtccTabRequest.traceName);
  }

  @Override
  public int hashCode() {
    return Objects.hash(assetId, filterPack, orderBy, page, snapDate, subGroupKeySearch, submissionId, traceName);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumDtccTabRequest {\n");
    sb.append("    assetId: ").append(toIndentedString(assetId)).append("\n");
    sb.append("    filterPack: ").append(toIndentedString(filterPack)).append("\n");
    sb.append("    orderBy: ").append(toIndentedString(orderBy)).append("\n");
    sb.append("    page: ").append(toIndentedString(page)).append("\n");
    sb.append("    snapDate: ").append(toIndentedString(snapDate)).append("\n");
    sb.append("    subGroupKeySearch: ").append(toIndentedString(subGroupKeySearch)).append("\n");
    sb.append("    submissionId: ").append(toIndentedString(submissionId)).append("\n");
    sb.append("    traceName: ").append(toIndentedString(traceName)).append("\n");
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
    openapiFields.add("assetId");
    openapiFields.add("filterPack");
    openapiFields.add("orderBy");
    openapiFields.add("page");
    openapiFields.add("snapDate");
    openapiFields.add("subGroupKeySearch");
    openapiFields.add("submissionId");
    openapiFields.add("traceName");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumDtccTabRequest
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumDtccTabRequest.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumDtccTabRequest is not found in the empty JSON string", TitaniumDtccTabRequest.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumDtccTabRequest.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumDtccTabRequest` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("assetId") != null && !jsonObj.get("assetId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `assetId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("assetId").toString()));
      }
      // validate the optional field `filterPack`
      if (jsonObj.getAsJsonObject("filterPack") != null) {
        TitaniumFilterPack.validateJsonObject(jsonObj.getAsJsonObject("filterPack"));
      }
      // validate the optional field `orderBy`
      if (jsonObj.getAsJsonObject("orderBy") != null) {
        TitaniumOrderBy.validateJsonObject(jsonObj.getAsJsonObject("orderBy"));
      }
      // validate the optional field `page`
      if (jsonObj.getAsJsonObject("page") != null) {
        TitaniumPage.validateJsonObject(jsonObj.getAsJsonObject("page"));
      }
      if (jsonObj.get("snapDate") != null && !jsonObj.get("snapDate").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `snapDate` to be a primitive type in the JSON string but got `%s`", jsonObj.get("snapDate").toString()));
      }
      // validate the optional field `subGroupKeySearch`
      if (jsonObj.getAsJsonObject("subGroupKeySearch") != null) {
        TitaniumSubGroupKeySearch.validateJsonObject(jsonObj.getAsJsonObject("subGroupKeySearch"));
      }
      if (jsonObj.get("submissionId") != null && !jsonObj.get("submissionId").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `submissionId` to be a primitive type in the JSON string but got `%s`", jsonObj.get("submissionId").toString()));
      }
      if (jsonObj.get("traceName") != null && !jsonObj.get("traceName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `traceName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("traceName").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumDtccTabRequest.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumDtccTabRequest' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumDtccTabRequest> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumDtccTabRequest.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumDtccTabRequest>() {
           @Override
           public void write(JsonWriter out, TitaniumDtccTabRequest value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumDtccTabRequest read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumDtccTabRequest given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumDtccTabRequest
  * @throws IOException if the JSON string is invalid with respect to TitaniumDtccTabRequest
  */
  public static TitaniumDtccTabRequest fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumDtccTabRequest.class);
  }

 /**
  * Convert an instance of TitaniumDtccTabRequest to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

