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
import java.math.BigDecimal;

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
 * TitaniumTradePeriodMetrics
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-20T18:30:09.225239Z[UTC]")
public class TitaniumTradePeriodMetrics {
  public static final String SERIALIZED_NAME_CURRENCY = "currency";
  @SerializedName(SERIALIZED_NAME_CURRENCY)
  private String currency;

  public static final String SERIALIZED_NAME_MAX_NOTIONAL_AMOUNT = "maxNotionalAmount";
  @SerializedName(SERIALIZED_NAME_MAX_NOTIONAL_AMOUNT)
  private BigDecimal maxNotionalAmount;

  public static final String SERIALIZED_NAME_MIN_NOTIONAL_AMOUNT = "minNotionalAmount";
  @SerializedName(SERIALIZED_NAME_MIN_NOTIONAL_AMOUNT)
  private BigDecimal minNotionalAmount;

  public static final String SERIALIZED_NAME_TOTAL_LIQUIDITY = "totalLiquidity";
  @SerializedName(SERIALIZED_NAME_TOTAL_LIQUIDITY)
  private BigDecimal totalLiquidity;

  public static final String SERIALIZED_NAME_TRADE_COUNT = "tradeCount";
  @SerializedName(SERIALIZED_NAME_TRADE_COUNT)
  private String tradeCount;

  public TitaniumTradePeriodMetrics() { 
  }

  public TitaniumTradePeriodMetrics currency(String currency) {
    
    this.currency = currency;
    return this;
  }

   /**
   * Get currency
   * @return currency
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getCurrency() {
    return currency;
  }


  public void setCurrency(String currency) {
    this.currency = currency;
  }


  public TitaniumTradePeriodMetrics maxNotionalAmount(BigDecimal maxNotionalAmount) {
    
    this.maxNotionalAmount = maxNotionalAmount;
    return this;
  }

   /**
   * Get maxNotionalAmount
   * @return maxNotionalAmount
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public BigDecimal getMaxNotionalAmount() {
    return maxNotionalAmount;
  }


  public void setMaxNotionalAmount(BigDecimal maxNotionalAmount) {
    this.maxNotionalAmount = maxNotionalAmount;
  }


  public TitaniumTradePeriodMetrics minNotionalAmount(BigDecimal minNotionalAmount) {
    
    this.minNotionalAmount = minNotionalAmount;
    return this;
  }

   /**
   * Get minNotionalAmount
   * @return minNotionalAmount
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public BigDecimal getMinNotionalAmount() {
    return minNotionalAmount;
  }


  public void setMinNotionalAmount(BigDecimal minNotionalAmount) {
    this.minNotionalAmount = minNotionalAmount;
  }


  public TitaniumTradePeriodMetrics totalLiquidity(BigDecimal totalLiquidity) {
    
    this.totalLiquidity = totalLiquidity;
    return this;
  }

   /**
   * Get totalLiquidity
   * @return totalLiquidity
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public BigDecimal getTotalLiquidity() {
    return totalLiquidity;
  }


  public void setTotalLiquidity(BigDecimal totalLiquidity) {
    this.totalLiquidity = totalLiquidity;
  }


  public TitaniumTradePeriodMetrics tradeCount(String tradeCount) {
    
    this.tradeCount = tradeCount;
    return this;
  }

   /**
   * Get tradeCount
   * @return tradeCount
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getTradeCount() {
    return tradeCount;
  }


  public void setTradeCount(String tradeCount) {
    this.tradeCount = tradeCount;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumTradePeriodMetrics titaniumTradePeriodMetrics = (TitaniumTradePeriodMetrics) o;
    return Objects.equals(this.currency, titaniumTradePeriodMetrics.currency) &&
        Objects.equals(this.maxNotionalAmount, titaniumTradePeriodMetrics.maxNotionalAmount) &&
        Objects.equals(this.minNotionalAmount, titaniumTradePeriodMetrics.minNotionalAmount) &&
        Objects.equals(this.totalLiquidity, titaniumTradePeriodMetrics.totalLiquidity) &&
        Objects.equals(this.tradeCount, titaniumTradePeriodMetrics.tradeCount);
  }

  @Override
  public int hashCode() {
    return Objects.hash(currency, maxNotionalAmount, minNotionalAmount, totalLiquidity, tradeCount);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumTradePeriodMetrics {\n");
    sb.append("    currency: ").append(toIndentedString(currency)).append("\n");
    sb.append("    maxNotionalAmount: ").append(toIndentedString(maxNotionalAmount)).append("\n");
    sb.append("    minNotionalAmount: ").append(toIndentedString(minNotionalAmount)).append("\n");
    sb.append("    totalLiquidity: ").append(toIndentedString(totalLiquidity)).append("\n");
    sb.append("    tradeCount: ").append(toIndentedString(tradeCount)).append("\n");
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
    openapiFields.add("currency");
    openapiFields.add("maxNotionalAmount");
    openapiFields.add("minNotionalAmount");
    openapiFields.add("totalLiquidity");
    openapiFields.add("tradeCount");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumTradePeriodMetrics
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumTradePeriodMetrics.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumTradePeriodMetrics is not found in the empty JSON string", TitaniumTradePeriodMetrics.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumTradePeriodMetrics.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumTradePeriodMetrics` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("currency") != null && !jsonObj.get("currency").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `currency` to be a primitive type in the JSON string but got `%s`", jsonObj.get("currency").toString()));
      }
      if (jsonObj.get("tradeCount") != null && !jsonObj.get("tradeCount").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `tradeCount` to be a primitive type in the JSON string but got `%s`", jsonObj.get("tradeCount").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumTradePeriodMetrics.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumTradePeriodMetrics' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumTradePeriodMetrics> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumTradePeriodMetrics.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumTradePeriodMetrics>() {
           @Override
           public void write(JsonWriter out, TitaniumTradePeriodMetrics value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumTradePeriodMetrics read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumTradePeriodMetrics given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumTradePeriodMetrics
  * @throws IOException if the JSON string is invalid with respect to TitaniumTradePeriodMetrics
  */
  public static TitaniumTradePeriodMetrics fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumTradePeriodMetrics.class);
  }

 /**
  * Convert an instance of TitaniumTradePeriodMetrics to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

